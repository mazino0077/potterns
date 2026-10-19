from abc import ABC, abstractmethod
from models import Computer


class IComputerBuilder(ABC):

  @abstractmethod
  def reset(self) -> None:
    pass

  @abstractmethod
  def set_cpu(self, cpu: str) -> "IComputerBuilder":
    pass

  @abstractmethod
  def set_ram(self, ram: str) -> "IComputerBuilder":
    pass

  @abstractmethod
  def set_gpu(self, gpu: str) -> "IComputerBuilder":
    pass

  @abstractmethod
  def set_ssd(self, ssd: str) -> "IComputerBuilder":
    pass

  @abstractmethod
  def set_os(self, os: str) -> "IComputerBuilder":
    pass

  @abstractmethod
  def build(self) -> Computer:
    pass


class ComputerBuilder(IComputerBuilder):

  def __init__(self):
    self.reset()

  def reset(self) -> None:
    self._computer = Computer()

  def set_cpu(self, cpu: str) -> "ComputerBuilder":
    self._computer.cpu = cpu
    return self

  def set_ram(self, ram: str) -> "ComputerBuilder":
    self._computer.ram = ram
    return self

  def set_gpu(self, gpu: str) -> "ComputerBuilder":
    self._computer.gpu = gpu
    return self

  def set_ssd(self, ssd: str) -> "ComputerBuilder":
    self._computer.ssd = ssd
    return self

  def set_os(self, os: str) -> "ComputerBuilder":
    self._computer.os = os
    return self

  def build(self) -> Computer:
    built_pc = self._computer
    self.reset()
    return built_pc