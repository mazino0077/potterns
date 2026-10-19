from builder import ComputerBuilder
from director import ComputerDirector


def main():
  builder = ComputerBuilder()

  # 1. Qo'lda (custom) yig'ish
  custom_pc = (
      builder.set_cpu("Intel Core i5-14600K")
      .set_ram("32GB DDR5")
      .set_ssd("1TB SSD")
      .set_os("Arch Linux")
      .set_gpu("NVIDIA GeForce RTX 4070 Ti")
      .build()
  )
  print(custom_pc)

  print("\n" + "=" * 40 + "\n")

  # 2. Director orqali tayyor profilni yig'ish
  director = ComputerDirector(builder)
  gaming_pc = director.build_gaming_pc()
  print(gaming_pc)


if __name__ == "__main__":
  main()