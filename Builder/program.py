# from typing import Optional



# class Computer:

#   def __init__(self):
#     self.cpu: Optional[str] = None
#     self.ram: Optional[str] = None
#     self.gpu: Optional[str] = None
#     self.ssd: Optional[str] = None
#     self.os: Optional[str] = None

#   def __str__(self) -> str:
#     return (
#         "Kompyuter spetsifikatsiyasi:\n"
#         f"  • CPU : {self.cpu or 'O‘rnatilmagan'}\n"
#         f"  • RAM : {self.ram or 'O‘rnatilmagan'}\n"
#         f"  • GPU : {self.gpu or 'O‘rnatilmagan'}\n"
#         f"  • SSD : {self.ssd or 'O‘rnatilmagan'}\n"
#         f"  • OS  : {self.os or 'O‘rnatilmagan'}"
#     )



# class ComputerBuilder:

#   def __init__(self):
#     self.reset()

#   def reset(self) -> None:
#     self._computer = Computer()

#   def set_cpu(self, cpu: str) -> "ComputerBuilder":
#     self._computer.cpu = cpu
#     return self  

#   def set_ram(self, ram: str) -> "ComputerBuilder":
#     self._computer.ram = ram
#     return self

#   def set_gpu(self, gpu: str) -> "ComputerBuilder":
#     self._computer.gpu = gpu
#     return self

#   def set_ssd(self, ssd: str) -> "ComputerBuilder":
#     self._computer.ssd = ssd
#     return self

#   def set_os(self, os: str) -> "ComputerBuilder":
#     self._computer.os = os
#     return self

#   def build(self) -> Computer:
#     built_pc = self._computer
#     self.reset() 
#     return built_pc



# class ComputerDirector:

#   def __init__(self, builder: ComputerBuilder):
#     self.builder = builder

#   def build_gaming_pc(self) -> Computer:
#     return (
#         self.builder.set_cpu("AMD Ryzen 7 7800X3D")
#         .set_ram("32GB DDR5 6000MHz")
#         .set_gpu("NVIDIA GeForce RTX 4080 Super")
#         .set_ssd("2TB NVMe M.2 SSD")
#         .set_os("Windows 11 Pro")
#         .build()
#     )

#   def build_office_pc(self) -> Computer:
#     return (
#         self.builder.set_cpu("Intel Core i3-13100")
#         .set_ram("16GB DDR4")
#         .set_gpu("Integrated Intel UHD")
#         .set_ssd("512GB NVMe SSD")
#         .set_os("Ubuntu 24.04 LTS")
#         .build()
#     )


# builder = ComputerBuilder()
# custom_pc = (
#     builder.set_cpu("Intel Core i5-14600K")
#     .set_ram("32GB DDR5")
#     .set_ssd("1TB SSD")
#     .set_os("Arch Linux")
#     .set_gpu("NVIDIA GeForce RTX 4070 Ti")
#     .build()
# )

# # print(custom_pc)
# a=ComputerDirector(builder)
# office_pc = a.build_office_pc()
# print(office_pc)