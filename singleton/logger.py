from threading import Lock


class ProgrammLogger:
    _programm_logger: "ProgrammLogger | None" = None
    _lock: Lock = Lock()

    def __new__(cls) -> "ProgrammLogger":
        if cls._programm_logger is None:
            with cls._lock:
                if cls._programm_logger is None:
                    instance = super().__new__(cls)
                    instance._log_entries = ["This is log file."]
                    cls._programm_logger = instance
        return cls._programm_logger

    @classmethod
    def get_programm_logger(cls) -> "ProgrammLogger":
        return cls()

    def add_log_info(self, info: str) -> None:
        with self._lock:
            self._log_entries.append(info)

    def show_log_info(self) -> None:
        print("\n".join(self._log_entries) + "\n")



if __name__ == "__main__":
    logger1 = ProgrammLogger.get_programm_logger()
    logger1.add_log_info("Starting math processing")
    logger1.add_log_info("Math processing success")
    logger1.show_log_info()

    logger2 = ProgrammLogger.get_programm_logger()
    logger2.show_log_info()

    print(logger1 is logger2) 