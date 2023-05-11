class RecommenderEngine:

    def __init__(self) -> None:
        self.model = None
        pass

    def handle_model_creation(self):
        '''
        Do model creation part
        Create the model, or load from the file
        ''' 
        pass

    def train(self):
        '''
        A wrapper for training if needed
        '''
        pass

    def predict(self) -> str:
        '''
        A wrapper for predicting if needed
        '''
        pass