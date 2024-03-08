# lf5-ls3-exercise
Contains the exercises of lf5\ls3 (Makler) such as r2d2, heron and alike

<table><tr><th><p>Ausbildung zum Fachinformatiker</p><p><b>Lernfeld 5 – Einführung in grundlegende Programmierkonzepte</b></p></th></tr>
<tr><td><i>Übungsaufgaben zu Anweisung, Verzweigung und Fallunterscheidung</i></td></tr>
</table>

# **Voraussetzung für diese Übungsaufgaben**

- Grundlagen der Programmierung in Python (IF/ELSE; While)
- Funktionen, Parameter, Argumente
- Tupel, ggfs. Arrays


# **Aufgabe 1: Simulation der Populationsentwicklung von R2-D2**
Erstellen Sie einen PAP/ ein Python-Programm zur Simulation der Populationsentwicklung von R2-D2-Robotern (mit etwas Fantasie ;-) anhand der folgenden Vorgaben:

- Unterteilung in drei Altersstufen: 
  junge R2-D2, erwachsene R2-D2 und alte R2-D2
- In jedem Schritt erfolgt ein Wechsel der Altersstufen oder die „galaktische Verschrottung“: Junge R2-D2 werden erwachsen, Erwachsene werden alt (und alte R2-D2 werden leider alle verschrottet…) 
- **Regeln zur Alterung:** Nur ein bestimmter Anteil erreicht die nächste Altersstufe. Nur jeder zweite Junge R2-D2 wird erwachsen (alle anderen werden verschrottet) und nur jeder dritte Erwachsene R2-D2 wird alt. 
- **Regeln zur Reproduktion:** Wir gehen weiter davon aus, dass jeder Erwachsene R2-D2 vier Junge R2-D2 konstruiert und dass jeder Alte R2-D2 zwei Junge R2-D2 konstruiert.

  ![](Images/Aspose.Words.cd7ee974-0d64-4e49-bb48-fc4e32b9d5c4.002.jpeg)

|**Schritt**|**Junge R2D2**|**Erwachsene R2D2**|**Alte R2D2**|
| :-: | :-: | :-: | :-: |
|1|10|10|10|
|2||||
|…|<p></p><p></p>|||
|<p></p><p></p>||||
|<p></p><p></p>||||
# ![](Images/Aspose.Words.cd7ee974-0d64-4e49-bb48-fc4e32b9d5c4.003.png)**Aufgabe 2: Streichholzspiel**
Das so genannte **Nim-Spiel** ist ein Spiel für zwei Personen, bei dem abwechselnd eine Anzahl von Gegenständen (z.B. Streichhölzer) weggenommen wird. Gewonnen hat derjenige, der den letzten Gegenstand nehmen muss.

Hintergrund: The Nimatron is a computer that allows one to play the game Nim. It was first presented in April 1940 at the 1939 New York World's Fair purely as a form of entertainment.
(Quelle: https://en.wikipedia.org/wiki/Nimatron)

**Implementieren Sie das Streichholzspiel in folgender Variante als PAP/ in Python.**

*Es sind 31 Streichhölzer gegeben. Die Spieler A (Computer) und B (Mensch) nehmen abwechselnd mindestens ein und höchstens sechs Streichhölzer. Spieler A (Computer) fängt an. Wer das letzte Streichholz nehmen muss, hat verloren.*

Algorithmus:

1. Spieler A nimmt 2 Streichhölzer
1. Spieler B nimmt beliebig 1 bis 6 Streichhölzer.
1. Spieler A nimmt eine ergänzende Anzahl, so dass insgesamt 7 entnommen werden.
1. Schritte 2 und 3 werden wiederholt bis nur noch ein Streichholz übrigbleibt.
1. Dieses Streichholz muss Spieler B nehmen, der dadurch verliert.

Optionale Varianten:
\- Der menschliche Spieler darf die Anzahl der Streichhölzer für den Start festlegen.
\- Der Computerspieler legt die Anzahl der Streichhölzer für den Start zufällig fest.


# **Aufgabe 3: Berechnung der Quadratwurzel (Heron-Verfahren)**
Das **Heron-Verfahren** (Heronsche Näherungsverfahren oder babylonische Wurzelziehen) ist ein Rechenverfahren zur Berechnung einer **Näherung der Quadratwurzel** einer reellen Zahl a > 0.
(Quelle https://de.wikipedia.org/wiki/Heron-Verfahren)

Dabei wird ein Rechteck so lange flächengleich verformt, bis beide Kanten a und b näherungsweise gleich sind – also das Rechteck zum Quadrat wird. Typisch für Näherungsverfahren ist, dass der gewünschte Wert nach mehren, gleichen Rechenschritten nur annäherungsweise erreicht wird und dass die Anzahl der Wiederholungen entscheidend dafür ist, wie genau das Ergebnis werden kann.

Ein Rechteck mit konstanter Fläche **F** hat zu Beginn die Kanten **a = F** (hier unten 25) und **b = 1**. Für die Näherung zum Quadrat hin wird mit jedem Schritt **a** verkleinert, indem es den **Mittelwert** von **a** und **b** des vorherigen Schrittes zugewiesen bekommt. Aus diesem Wert und der konstanten Fläche **F** wird der passende Wert für **b** bestimmt durch **b = F/a**. Ferner wird die **Abweichung** von **a** und **b** bestimmt. Wir wollen mit dem Schritt zufrieden sein, bei dem die **Abweichung** unter den Wert **0,01** gekommen ist. Der **Näherungswert** für die **Wurzel** lässt sich aus **a** in diesem Schritt ablesen.

Aufgabe:

- Führen Sie für den Algorithmus als Textrezept einen Schreibtischtest durch
- Erstellen Sie einen PAP dafür
- Codieren Sie ein passendes Python-Program
  Variablen: ***laenge\_a, laenge\_b, mittelwert, abweichung***
- Führen mit dem Python-Programm einen Schreibtischtest durch
- Erkunden Sie den Debugger ihrer Entwicklungsumgebung mit ihrem Programm

|Rechenverfahren|Geometrische Visualisierung|
| :- | :- |
|||

|** |**Länge a**|**Länge b**|**Mittelwert**|**Abweichung**|
| :- | :-: | :-: | :-: | :-: |
|1|25|1|13|24|
||||||
||||||
||||||
||||||
||||||

||![](Images/Aspose.Words.cd7ee974-0d64-4e49-bb48-fc4e32b9d5c4.004.png)	|
| :- | :- |

# **Aufgabe 4: Berechnung der Quersumme einer Zahl**
Das folgende Python-Programm berechnet die Quersumme einer eingegebenen Zahl. Erstellen Sie zu Dokumentationszwecken einen Programmablaufplan und machen Sie den Schreibtischtest (der Ausgaben in den Zeilen 13/14) für die **Zahl 362**.

![](Images/Aspose.Words.cd7ee974-0d64-4e49-bb48-fc4e32b9d5c4.005.png)

|**exponent**|**temp\_value**|**checksum**|**number**|
| :-: | :-: | :-: | :-: |
|<p></p><p></p>||||
|<p></p><p></p>||||
|<p></p><p></p>||||
|<p></p><p></p>||||

LS-5.3-Übungsaufgaben-v5.docx	1	EG,FE,FN -  21.02.2024

