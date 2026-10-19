from builder import HttpClientBuilder


def main():
  builder = HttpClientBuilder()

  internal_api_client = (
      builder.set_base_url("https://api.myapp.com/v1")
      .set_timeout(5.0)
      .set_bearer_token("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...")
      .add_header("X-Service-Name", "OrderService")
      .set_retries(2)
      .build()
  )

  internal_api_client.get("/users", params={"page": 1, "limit": 20})

  print("\n" + "=" * 50 + "\n")

  public_client = (
      builder.set_base_url("https://open-data.example.com")
      .set_timeout(15.0)
      .set_verify_ssl(False)
      .build()
  )

  public_client.post("/feedback", json_data={"rating": 5, "comment": "Great!"})


if __name__ == "__main__":
  main()