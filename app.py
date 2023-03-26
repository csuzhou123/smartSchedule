from flask import Flask

app = Flask(__name__)
class ObseravtionTask:

    def __init__(self):
        self._id = '63f42e11312f5f32f083505b'
        self.id = '1'
        self.startlatitude = '0.0'
        self.endlatitude = '0.0'
        self.startLongitude = '0.0'
        self.endLongitude = '0.0'
        self.scheduleId = '1'


class ObservationResultDTO:
    def __init__(self):
        self.id = '1'
        self.satellliteId = '1'
        self.ObseravtionTask = None
        self.startTime = '2000.1.1 1:48:50'
        self.endTime = '2000.1.1 15:54:0'

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/observation/solution/<scheduleId>/swarms')
def swarms_solution(scheduleId):
    result = []

    observationResult = ObservationResultDTO()
    result.append(observationResult)

    return result

if __name__ == '__main__':
    app.run()
