from pathlib import Path

from server.server import app

__all__ = ["app"]

if __name__ == "__main__":
    import uvicorn

    module = Path(__file__).stem
    uvicorn.run(
        f"{module}:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        # access_log=False,
        reload_excludes="logs",
        workers=1,
    )
from pathlib import Path

from server.server import app

__all__ = ["app"]

if __name__ == "__main__":
    import uvicorn

    module = Path(__file__).stem
    uvicorn.run(
        f"{module}:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        # access_log=False,
        workers=1,
    )
