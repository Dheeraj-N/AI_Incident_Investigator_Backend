class InvestigationException(
    Exception
):

    def __init__(
        self,
        message: str
    ):
        self.message = message

        super().__init__(
            message
        )


class IncidentNotFoundError(
    InvestigationException
):
    pass


class CoralQueryFailedError(
    InvestigationException
):
    pass


class TimelineBuildFailedError(
    InvestigationException
):
    pass


class GeminiRateLimitError(
    InvestigationException
):
    pass