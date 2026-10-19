from builder import IComputerBuilder
from models import Computer


class ComputerDirector:

  def __init__(self, builder: IComputerBuilder):
    self.builder = builder

  def build_gaming_pc(self) -> Computer:
    return (
        self.builder.set_cpu("AMD Ryzen 7 7800X3D")
        .set_ram("32GB DDR5 6000MHz")
        .set_gpu("NVIDIA GeForce RTX 4080 Super")
        .set_ssd("2TB NVMe M.2 SSD")
        .set_os("Windows 11 Pro")
        .build()
    )

  def build_office_pc(self) -> Computer:
    return (
        self.builder.set_cpu("Intel Core i3-13100")
        .set_ram("16GB DDR4")
        .set_gpu("Integrated Intel UHD")
        .set_ssd("512GB NVMe SSD")
        .set_os("Ubuntu 24.04 LTS")
        .build()
    )