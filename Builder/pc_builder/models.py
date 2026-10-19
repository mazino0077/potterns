from typing import Optional


class Computer:

  def __init__(self):
    self.cpu: Optional[str] = None
    self.ram: Optional[str] = None
    self.gpu: Optional[str] = None
    self.ssd: Optional[str] = None
    self.os: Optional[str] = None

  def __str__(self) -> str:
    return (
        "Kompyuter spetsifikatsiyasi:\n"
        f"  • CPU : {self.cpu or 'O‘rnatilmagan'}\n"
        f"  • RAM : {self.ram or 'O‘rnatilmagan'}\n"
        f"  • GPU : {self.gpu or 'O‘rnatilmagan'}\n"
        f"  • SSD : {self.ssd or 'O‘rnatilmagan'}\n"
        f"  • OS  : {self.os or 'O‘rnatilmagan'}"
    )