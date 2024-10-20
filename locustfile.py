import time
from locust import HttpUser, TaskSet, task, between
from locust.exception import LocustError
from tavern.core import run
from pytest import ExitCode

class UserBehavior(TaskSet):
    @task
    def run_tavern_test(self):
        try:

            start_time = time.time()

            exit_code = run("test_server.tavern.yaml")

            response_time = int((time.time() - start_time) * 1000)

            if exit_code != ExitCode.OK:
                raise Exception("Tavern Test failed!")
            else:
                print("Tavern test passed!")


                # Fire a success event
                self.user.environment.events.request.fire(
                    request_type="tavern",
                    name="run_tavern_test",
                    response_time=response_time, # Use total duration, could also extract more precice from pytest meta data
                    response_length=0,
                    response=None,
                    context={},
                    exception=None # No exception to indicate success
                )



        except Exception as e:
            print(f"Tavern test failed: {e}")

            # Fire a failure event
            self.user.environment.events.request.fire(
                request_type="tavern",
                name="run_tavern_test",
                response_time=response_time,
                response_length=0,
                response=None,
                context={},
                exception=e
            )


            raise LocustError(f"Tavern test failed: {e}")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    #min_wait = 1000
    #max_wait = 2000
    wait_time = between (0.5,1)

