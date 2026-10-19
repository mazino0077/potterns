from builder import ComputerBuilder
from director import ComputerDirector


def main():
  builder = ComputerBuilder()

  custom_pc = (
      builder.set_cpu("Intel Core i5-14600K")
      .set_ram("32GB DDR5")
      .set_ssd("1TB SSD")
      .set_os("Arch Linux")
      .set_gpu("NVIDIA GeForce RTX 4070 Ti")
      .build()
  )
  print(custom_pc)

