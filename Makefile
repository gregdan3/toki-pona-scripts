init: nimi_pu.txt nimi_pi_pu_ala.txt compounds.txt
process: nimi.json

nimi_pu.txt:
	curl -s https://tokipona.org/nimi_pu.txt > nimi_pu.txt
nimi_pi_pu_ala.txt:
	curl -s https://tokipona.org/nimi_pi_pu_ala.txt > nimi_pi_pu_ala.txt
compounds.txt:
	curl -s https://tokipona.org/compounds.txt > compounds.txt
nimi.json: nasin_e_nimi.py nimi_pu.txt nimi_pi_pu_ala.txt nimi_ku.txt
	python ./nasin_e_nimi.py | jq > nimi.json
nimi_lili.json: nasin_e_nimi.py nimi_pu.txt nimi_pi_pu_ala.txt nimi_ku.txt
	python ./nasin_e_nimi.py --maxsize=4 --minscore=40 | jq > nimi_lili.json

clean:
	rm nimi_pu.txt nimi_pi_pu_ala.txt compounds.txt nimi.json nimi_lili.json
