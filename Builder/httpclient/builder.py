from typing import Dict
from client import HttpClient


class HttpClientBuilder:

  def __init__(self):
    self.reset()

  def reset(self) -> "HttpClientBuilder":
    self._base_url: str = ""
    self._timeout: float = 10.0
    self._headers: Dict[str, str] = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    self._retries: int = 3
    self._verify_ssl: bool = True
    return self

  def set_base_url(self, base_url: str) -> "HttpClientBuilder":
    if not base_url.startswith(("http://", "https://")):
      raise ValueError("Base URL 'http://' yoki 'https://' bilan boshlanishi shart")
    self._base_url = base_url
    return self

  def set_timeout(self, timeout: float) -> "HttpClientBuilder":
    if timeout <= 0:
      raise ValueError("Timeout qiymati 0 dan katta bo'lishi kerak")
    self._timeout = timeout
    return self

  def add_header(self, key: str, value: str) -> "HttpClientBuilder":
    self._headers[key] = value
    return self

  def set_bearer_token(self, token: str) -> "HttpClientBuilder":
    self._headers["Authorization"] = f"Bearer {token}"
    return self

  def set_retries(self, retries: int) -> "HttpClientBuilder":
    if retries < 0:
      raise ValueError("Retries soni manfiy bo'lishi mumkin emas")
    self._retries = retries
    return self

  def set_verify_ssl(self, verify: bool) -> "HttpClientBuilder":
    self._verify_ssl = verify
    return self

  def build(self) -> HttpClient:
    if not self._base_url:
      raise ValueError("Mijozni yaratish uchun base_url kiritilishi shart")

    client = HttpClient(
        base_url=self._base_url,
        timeout=self._timeout,
        headers=dict(self._headers),
        retries=self._retries,
        verify_ssl=self._verify_ssl,
    )
    self.reset()
    return client