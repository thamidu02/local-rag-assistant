from abc import ABC,abstractmethod

class BasedocumentLoader(ABC):
    
    @abstractmethod
    def load(self,file_path:str)->str:
        """
        Load a document and return extracted test
        """
        pass
        