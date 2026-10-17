class ProgrammLogger:
    _instance = None
    _log_file: str = "This is log file.\n\n"

    # Java'dagi getProgrammLogger() va private konstruktor o'rnini bosadi
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    # Agar Java uslubida chaqirishni xohlasangiz, staticmethod ham qo'shish mumkin:
    @classmethod
    def get_programm_logger(cls) -> "ProgrammLogger":
        return cls()

    def add_log_info(self, log_info: str) -> None:
        self._log_file += f"{log_info}\n"

    def show_log_info(self) -> None:
        print(self._log_file)


# --- main() qismi ---
if __name__ == "__main__":
    # 1-obyektni olamiz (ProgrammLogger() yoki ProgrammLogger.get_programm_logger())
    programm_logger = ProgrammLogger.get_programm_logger()
    programm_logger.add_log_info("Starting math processing")
    programm_logger.add_log_info("Math processing success")
    programm_logger.show_log_info()

    # 2-obyektni olamiz
    programm_logger2 = ProgrammLogger.get_programm_logger()
    programm_logger2.show_log_info()

    # Ikkalasi bitta obyekt ekanligini tekshiramiz
    print("Equals (==):", programm_logger == programm_logger2)  # True
    print("Same object (is):", programm_logger is programm_logger2)  # True