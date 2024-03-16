# Importar las clases necesarias
from datetime import date
from anuncio import Video, Display, Social
from error import LargoExcedidoError

class Campania():
    def __init__(self, nombre: str, fecha_inicio: date,
                 fecha_termino: date, anuncios: list) -> None:
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = [self.__obtener_instancia_anuncio(a) for a in anuncios]

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, value: str) -> None:
        if len(value) <= 250:
            self.__nombre = value
        else:
            raise LargoExcedidoError("El nombre de la campaña excede los 250 caracteres")

    @property
    def fecha_inicio(self) -> date:
        return self.__fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, value: date) -> None:
        self.__fecha_inicio = value

    @property
    def fecha_termino(self) -> date:
        return self.__fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, value: date) -> None:
        self.__fecha_termino = value

    @property
    def anuncios(self) -> list:
        return self.__anuncios

    def __str__(self):
        cant_video = sum(1 for anuncio in self.anuncios if isinstance(anuncio, Video))
        cant_display = sum(1 for anuncio in self.anuncios if isinstance(anuncio, Display))
        cant_social = sum(1 for anuncio in self.anuncios if isinstance(anuncio, Social))

        return (f"Nombre de la Campaña: {self.__nombre}\n"
                f"Anuncios: {cant_video} Video, "
                f"{cant_display} Display, "
                f"{cant_social} Social")

    def __obtener_instancia_anuncio(self, anuncio: dict):
        tipo_anuncio = anuncio.get("tipo", "").lower()
        ancho = anuncio.get("ancho", 0)
        alto = anuncio.get("alto", 0)
        url_archivo = anuncio.get("url_archivo", "")
        url_clic = anuncio.get("url_clic", "")
        sub_tipo = anuncio.get("sub_tipo", "")
        duracion = anuncio.get("duracion", 0)

        if tipo_anuncio == "video":
            return Video(url_archivo, url_clic, sub_tipo, duracion)
        elif tipo_anuncio == "social":
            return Social(ancho, alto, url_clic, url_clic, sub_tipo)
        else:
            return Display(ancho, alto, url_clic, url_clic, sub_tipo)
