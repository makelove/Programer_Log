# 3-1-世界语言-翻译-Siri朗读


- 视频 ？

- 百度翻译api
    - [通用翻译API接入文档](http://api.fanyi.baidu.com/doc/21)
-  Python调用macOS Siri [Python Text to Speech in Macintosh](https://stackoverflow.com/questions/12758591/python-text-to-speech-in-macintosh)


- 翻译请求限制


- 结果

```
(.py3) localhost:~ play$ py /Users/play/github/Machine_Translation_Subtitles_Group/src/macOS-siri-百度翻译-TTS.py
请输入中文:国际和平，让和平白鸽自由飞翔，带去安宁温馨；让美好橄榄枝四处蔓延，编织幸福世界；让和谐旗帜随风飘扬，传递快乐心语。祝愿世界和平，永无战争！

普通话
台湾
香港
en   com.apple.speech.synthesis.voice.Alex
International peace, let peace dove fly freely, bring peace and warmth; let the olive branch spread everywhere, weave a happy world; let the harmonious flag fly with the wind, convey happy words. Wish the world peace and never war!
----------------------------------------
ru   com.apple.speech.synthesis.voice.milena
международный мир, мир белых голубей, мир, свобода летать, мир и тепло, великолепные оливковые ветви, сплетая счастливый мир, и гармоничные флаги, развевающиеся по ветру, передают радость.Пусть мир во всем мире, никогда не будет войны!
----------------------------------------
ara      com.apple.speech.synthesis.voice.tarik
السلام الدولي ، واسمحوا حمامة بيضاء سلمية تطير بحرية ، تأخذ راحة البال و الدفء ، واسمحوا جيدة غصين الزيتون تنتشر في جميع أنحاء العالم ، نسج السعادة ، اسمحوا الوئام راية ترفرف في مهب الريح ، تمرير سعيدالسلام في العالم ، لا حرب
----------------------------------------
hu   com.apple.speech.synthesis.voice.mariska
A nemzetközi béke, hadd repüljön szabadon a békegalamb, hozzon békét és meleget; az olajág terjesszen mindenfelé, alakítson boldog világot; a harmonikus zászló repüljön a széllel, adjon boldog szavakat.Kívánj békét a világnak és soha ne háborúzz!
----------------------------------------
nl   com.apple.speech.synthesis.voice.ellen
Internationale vrede, laat de vrede vrij vliegen, breng vrede en warmte; laat de olijftak zich overal verspreiden, weven een gelukkige wereld; laat de harmonieuze vlag met de wind vliegen, breng gelukkige woorden.Wens de wereld vrede en nooit oorlog!
----------------------------------------
el   com.apple.speech.synthesis.voice.melina
Διεθνής ειρήνη, ας πετάξει το περιστέρι της ειρήνης ελεύθερα, να φέρει ειρήνη και ζεστασιά, ας απλωθεί το κλαδί της ελιάς παντού, να υφαίνει έναν ευτυχισμένο κόσμο, ας πετάξει η αρμονική σημαία με τον άνεμο, να μεταφέρει χαρούμενα λόγια.Ευχήσου στον κόσμο ειρήνη και ποτέ πόλεμο!
----------------------------------------
dan      com.apple.speech.synthesis.voice.sara
International fred, lad fredsdue flyve frit, bringe fred og varme, lad olivengrenen sprede sig overalt, væve en lykkelig verden, lad det harmoniske flag flyve med vinden, overbringe glade ord.Ønsk verden fred og aldrig krig!
----------------------------------------
spa      com.apple.speech.synthesis.voice.Jorge
Paz internacional: que las palomas de la paz puedan volar libremente y llevar paz y tranquilidad; que las bellas ramas de olivo se extiendan por todas partes para tejer un mundo de felicidad; que las banderas de la armonía ondeen con el viento y transmitan la felicidad.¡Que el mundo sea pacífico y no haya guerra!
2020-03-01 16:04:16.270 python[15212:642205] NSSpeechSynthesizer: [NSSpeechSynthesizer setVoice:] - Voice identifier not found.
----------------------------------------
it   com.apple.speech.synthesis.voice.alice
La pace internazionale, la colomba di pace vola liberamente, porta pace e calore; che il ramo d'ulivo si diffonda ovunque, tessa un mondo felice; che la bandiera armoniosa voli con il vento, trasmetta parole felici.Auguri al mondo pace e mai guerra!
----------------------------------------
kor      com.apple.speech.synthesis.voice.yuna
평화 평화, 평화 비둘기 자유 비상, 평화 평화 평화 평화 평화 평화 평화 를 데리고 안녕 훈훈한 향기 를 전달 했 다.세계 평화를 기원하고 영원히 전쟁이 없기를 기원합니다!
----------------------------------------
de   com.apple.speech.synthesis.voice.anna
Internationaler Frieden, lasst die Friedenstaube frei fliegen, bringt Frieden und Wärme; lasst den Olivenzweig sich überall ausbreiten, weben eine glückliche Welt; lasst die harmonische Flagge mit dem Wind wehen, überbringen glückliche Worte.Wünsch der Welt Frieden und niemals Krieg!
----------------------------------------
pl   com.apple.speech.synthesis.voice.zosia
Międzynarodowy pokój, niech pokój gołąb swobodnie latać, przynieść pokój i ciepło; niech gałązka oliwna rozprzestrzenia się wszędzie, spleć szczęśliwy świat; niech harmonijna flag a powiewa z wiatrem, przekazać szczęśliwe słowa.Życz światu pokoju i nigdy wojny!
----------------------------------------
pt   com.apple.speech.synthesis.voice.joana
Paz internacional, que a pomba Da paz VOE livremente, traga Paz e calor; que o Ramo de Oliveira se espalhe por todo o lado, tecer um Mundo feliz; que a Bandeira harmoniosa VOE com o vento, transmita Palavras felizes.Deseje Paz Ao Mundo e Nunca guerra!
----------------------------------------
rom      com.apple.speech.synthesis.voice.ioana
Pacea internaţională, pacea să zboare liber, să aducă pace şi căldură; să se răspândească ramura de măslin peste tot, să ţesă o lume fericită; să zboare steagul armonios cu vântul, să transmită cuvinte fericite.Doresc pacea mondială și niciodată război!
----------------------------------------
slo      com.apple.speech.synthesis.voice.laura
Mednarodni mir, naj mirovna golobica prosto leti, naj prinese mir in toploto; naj se oljčna veja razširi povsod, naj splete srečen svet; naj harmonična zastava plapola z vetrom, naj posreduje srečne besede.Zaželi svetu mir in nikoli vojne!
----------------------------------------
th   com.apple.speech.synthesis.voice.kanya
สันติภาพระหว่างประเทศให้นกพิราบสีขาวบินได้อย่างอิสระและนำความสงบสุขและความอบอุ่นให้กิ่งมะกอกที่ดีกระจายไปทั่วโลกมีความสุขให้ธงสามัคคีบินกับลมและถ่ายทอดความสุข ขอให้สันติภาพของโลกไม่มีสงคราม
----------------------------------------
fin      com.apple.speech.synthesis.voice.satu
Kansainvälinen rauha, syöksyköön rauha vapaasti, tuokoon rauhaa ja lämpöä, levittäköön oliivioksa kaikkialle, kutoon onnellista maailmaa, tehköön harmoninen lippu tuulen kanssa, välittäköön iloisia sanoja.Toivokaa rauhaa, älkääkä koskaan sotiko!
----------------------------------------
fra      com.apple.speech.synthesis.voice.thomas
La paix internationale, la liberté des colombes de la paix de voler et d 'emporter dans la paix et la douceur; la propagation des branches d' Olivier de la beauté et l 'édification d' un monde heureux; le drapeau de l 'harmonie flotte au vent et transmet des paroles de joie.Que la paix règne dans le monde, jamais la guerre!
----------------------------------------
cs   com.apple.speech.synthesis.voice.zuzana
Mezinárodní mír, a ť mír volně létá, ať přinese mír a teplo; ať se olivová větev rozšíří všude, tkají šťastný svět; ať harmonická vlajka vlaje s větrem, ať nesou šťastná slova.Přeji světu mír a nikdy válku!
----------------------------------------
swe      com.apple.speech.synthesis.voice.alva
Internationell fred, låt fredsduvan flyga fritt, ge fred och värme; låt olivkvisten sprida sig överallt, väva en lycklig värld; låt den harmoniska flaggan flyga med vinden, förmedla glada ord.Önska världen fred och aldrig krig!
----------------------------------------
jp   com.apple.speech.synthesis.voice.kyoko
国際平和、平和のハトを自由に飛翔させ、安らぎと暖かさを持って行きます。美しいオリーブの枝があちこちに広がって、幸せな世界を作ります。調和の旗が風に翻り、楽しい心の言葉を伝えます。世界の平和を祈って、永遠に戦争がありません。
----------------------------------------
(.py3) localhost:~ play$ 
```
