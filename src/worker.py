#!/usr/bin/env python3

"""
copyright (c), 2021 antlas
"""


from typing import Any
import time

from .argument_parser import ArgumentParser
from .configuration import Configuration
from .importer import Importer
from .analyser import Analyser
from .exporter import Exporter
from .fsm import FiniteStateMachine


class Worker():
    def __init__(self):
        self._config = Configuration()
        self._ap = ArgumentParser("Reporter")
        self._ap.run()
        cfg = self._ap.get_args()
        self._config.read_configuration(cfg["configuration_file"])
        self._update_configuration_from_parser()
        self._fsm = None
        self._config.print_configuration()

    def _update_configuration_from_parser(self) -> None:
        """
        Update the configuration object from the command line parameters
        """
        ap_config = self._ap.get_args()
        cfg = self._config.get_config()

        if ap_config["input_directory"] is not None:
            cfg["input"]["directory"] = ap_config["input_directory"]
        if ap_config["output_directory"] is not None:
            cfg["output"]["directory"] = ap_config["output_directory"]

    def setup(self) -> None:
        """
        Setup the FSM before launching
        """
        self._fsm = self._create_fsm()

    def _create_fsm(self) -> FiniteStateMachine:
        """
        Create the FSM that will download data, analyse it and
        export results from it
        """
        def _fsm_start(dummy: Any):
            """
            Entry point of the state machine
            """
            return ("importing", dummy)

        def _fsm_import(config: dict):
            """
            State which imports the data
            """
            importer = Importer(config)
            try:
                data = importer.run()
            except Exception as e:
                return ("error", str(e))
            else:
                return ("analysing", (config, data))

        def _fsm_analyse(args):
            """
            Generate the analysis

            config: dict
            data:ImportFormat
            """
            config, data = args
            analyser = Analyser(config, data)
            try:
                result = analyser.run()
            except Exception as e:
                return ("error", str(e))
            else:
                return ("exporting", (config, result))

        def _fsm_export(args):
            """
            Export the result according to the config

            config: dict
            data:ExportFormat
            """
            config, data = args
            exporter = Exporter(config, data)
            try:
                exporter.run()
            except Exception as e:
                return ("error", str(e))
            else:
                return ("waiting", config)

        def _fsm_wait(config: dict):
            """
            Wait if necessary
            """
            should_wait, nap_time = [False, 0]  # check configuration
            if should_wait:
                time.sleep(nap_time)
                return ("importing", config)
            else:
                return ("end", None)

        def _fsm_error(message: str):
            """
            Error state, handle the error
            """
            print(message)

        def _fsm_end(dummy: Any):
            """
            End state, work done successfully
            """
            pass

        fsm = FiniteStateMachine()
        fsm.add_state("start", _fsm_start)
        fsm.add_state("importing", _fsm_import)
        fsm.add_state("analysing", _fsm_analyse)
        fsm.add_state("exporting", _fsm_export)
        fsm.add_state("waiting", _fsm_wait)
        fsm.add_state("end", _fsm_end, end_state=True)
        fsm.add_state("error", _fsm_error, end_state=True)
        fsm.set_start("start")

        return fsm

    def run(self) -> None:
        """
        Launch the program
        """
        fsm = self._create_fsm()
        fsm.set_doi(self._config.get_config())
        fsm.start()
