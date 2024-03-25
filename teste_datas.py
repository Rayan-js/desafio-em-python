import locale
from time import time
from datetime import datetime, timedelta
from tzlocal import get_localzone  # pip install tzlocal
import calendar
locale.setlocale(locale.LC_ALL, "pt_br")


class Zonyas:
    def __init__(self, dia=0) -> None:
        self.dia = timedelta(dia)
        self.dayObj = self.dia + datetime.now(get_localzone())

    def ultimo_dia_do_mes(self, ano, mes):
        ultimo_dia = calendar.monthrange(ano, mes)[1]
        last_day = datetime(ano, mes, ultimo_dia)
        return last_day.strftime("%d")

    def week_days(self):
        day = self.dayObj
        
        # Dia da semana
        dia_da_semana = day.strftime("%A").capitalize()
        # Dia do mês
        dia_do_mes = day.strftime("%d de %B")
        # Dia
        dia = day.strftime("%d")
        # Mês extenso
        mes_extenso = day.strftime("%B")
        # Mês
        mes = day.strftime("%m")
        # Ano
        ano = day.strftime("%Y")
        # Hora
        hora = day.strftime("%H")
        # Minuto
        minuto = day.strftime("%M")

        # Último dia do mês
        ultimo_dia = str(self.ultimo_dia_do_mes(ano=int(ano), mes=int(mes)))

        return dia, dia_da_semana, dia_do_mes, ultimo_dia,  mes, mes_extenso, ano, hora, minuto