from app.core.logger import logger


class CoralClient:
    async def execute(self, sql: str):
        logger.info("Executing Coral query")

        return {"status": "success", "data": []}
