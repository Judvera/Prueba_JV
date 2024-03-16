from abc import ABC, abstractmethod
from error import SubTipoInvalidoError

class Anuncio(ABC):
    def __init__(self, ancho: int, alto: int, url_archivo: str,
                 url_clic: str, sub_tipo: str) -> None:
        self.__ancho = ancho if ancho > 0 else 1
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo

    @property
    def ancho(self) -> int:
        return self.__ancho

    @ancho.setter
    def ancho(self, value: int) -> None:
        self.__ancho = value if value > 0 else 1

    @property
    def alto(self) -> int:
        return self.__alto

    @alto.setter
    def alto(self, value: int) -> None:
        self.__alto = value if value > 0 else 1

    @property
    def url_archivo(self) -> str:
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo(self, value: str) -> None:
        self.__url_archivo = value

    @property
    def url_clic(self) -> str:
        return self.__url_clic

    @url_clic.setter
    def url_clic(self, value: str) -> None:
        self.__url_clic = value

    @property
    def sub_tipo(self) -> str:
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, value: str) -> None:
        if value in self.SUB_TIPOS:
            self.__sub_tipo = value
        else:
            raise SubTipoInvalidoError("El sub tipo indicado no está permitido para este formato")

    @staticmethod
    def mostrar_formatos() -> None:
        print("FORMATO VIDEO:")
        print("==============")
        for v in Video.SUB_TIPOS:
            print(f"- {v}")

        print("FORMATO DISPLAY:")
        print("==============")
        for d in Display.SUB_TIPOS:
            print(f"- {d}")

        print("FORMATO SOCIAL:")
        print("==============")
        for s in Social.SUB_TIPOS:
            print(f"- {s}")

    @abstractmethod
    def comprimir_anuncios(self) -> None:
        pass

    @abstractmethod
    def redimensionar_anuncio(self) -> None:
        pass

class Video(Anuncio):
    SUB_TIPOS = ("instream", "outstream", "bumper")

    def __init__(self, url_archivo: str, url_clic: str, sub_tipo: str, duracion: int) -> None:
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        self.__duracion = duracion if duracion > 0 else 5

    @property
    def duracion(self) -> int:
        return self.__duracion

    @duracion.setter
    def duracion(self, value: int) -> None:
        self.__duracion = value if value > 0 else 5

    def comprimir_anuncios(self) -> None:
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self) -> None:
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

class Display(Anuncio):
    SUB_TIPOS = ("banner", "interstitial", "pop-up")

    def comprimir_anuncio(self) -> None:
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self) -> None:
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

class Social(Anuncio):
    SUB_TIPOS = ("historia", "publicacion", "evento")

    def comprimir_anuncio(self) -> None:
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self) -> None:
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
