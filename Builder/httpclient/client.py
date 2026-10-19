from typing import Any, Dict, Optional


class HttpClient:

  def __init__(
      self,
      base_url: str,
      timeout: float,
      headers: Dict[str, str],
      retries: int,
      verify_ssl: bool,
  ):
    self.base_url = base_url.rstrip("/")
    self.timeout = timeout
    self.headers = headers
    self.retries = retries
    self.verify_ssl = verify_ssl

  def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> None:
    url = f"{self.base_url}/{endpoint.lstrip('/')}"
    # Haqiqiy loyihada bu yerda httpx yoki requests orqali so'rov ketadi
    print(f"[GET] -> {url}")
    print(f"  Timeout: {self.timeout}s | SSL: {self.verify_ssl}")
    print(f"  Headers: {self.headers}")
    if params:
      print(f"  Params : {params}")

  def post(self, endpoint: str, json_data: Optional[Dict[str, Any]] = None) -> None:
    url = f"{self.base_url}/{endpoint.lstrip('/')}"
    print(f"[POST] -> {url}")
    print(f"  Timeout: {self.timeout}s | SSL: {self.verify_ssl}")
    print(f"  Headers: {self.headers}")
    if json_data:
      print(f"  Body   : {json_data}")