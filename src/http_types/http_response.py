class HttpResponse:
   def __init__(self, body, status_code: int) -> None:
      self.body = body
      self.status_code = status_code