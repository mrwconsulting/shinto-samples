import os
from aws_cdk import (
    aws_events as events,
    aws_lambda as lambda_,
    aws_events_targets as targets,
    App, Duration, Environment, Stack
)

class CdkPythonStack(Stack):
    def __init__(self, app: App, id: str, **kwargs) -> None:
        super().__init__(app, id, **kwargs)

        with open("lambda-handler.py", encoding="utf8") as fp:
            handler_code = fp.read()

        lambdaFn = lambda_.Function(
            self, "Singleton",
            code=lambda_.InlineCode(handler_code),
            handler="index.main",
            timeout=Duration.seconds(300),
            runtime=lambda_.Runtime.PYTHON_3_7,
        )

        rule = events.Rule(
            self, "Rule",
            schedule=events.Schedule.cron(
                minute='0',
                hour='18',
                month='*',
                week_day='MON-FRI',
                year='*'),
        )
        rule.add_target(targets.LambdaFunction(lambdaFn))

app = App()
default_region=os.getenv('AWS_REGION')
default_account=os.getenv('AWS_ACCOUNT')
CdkPythonStack(app, "cdk-python-stack",
    env=Environment(region=os.getenv('TARGET_REGION',default_region),account=os.getenv('TARGET_ACCOUNT',default_account)),
)
app.synth()
