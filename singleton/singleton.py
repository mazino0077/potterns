class ProgrammLogger:
    _instance = None
    _log_file: str = "This is log file.\n\n"


    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


    @classmethod
    def get_programm_logger(cls) -> "ProgrammLogger":
        return cls()

    def add_log_info(self, log_info: str) -> None:
        self._log_file += f"{log_info}\n"

    def show_log_info(self) -> None:
        print(self._log_file)



if __name__ == "__main__":

    programm_logger = ProgrammLogger.get_programm_logger()
    programm_logger.add_log_info("Starting math processing")
    programm_logger.add_log_info("Math processing success")
    programm_logger.show_log_info()

    programm_logger2 = ProgrammLogger.get_programm_logger()
    programm_logger2.show_log_info()

  
    print("Equals (==):", programm_logger == programm_logger2)  # True
    print("Same object (is):", programm_logger is programm_logger2)  # True