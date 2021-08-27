init: nimi_pu.txt nimi_pi_pu_ala.txt compounds.txt
process: nimi.json

nimi_pu.txt:
	curl -s https://tokipona.org/nimi_pu.txt > nimi_pu.txt
nimi_pi_pu_ala.txt:
	curl -s https://tokipona.org/nimi_pi_pu_ala.txt > nimi_pi_pu_ala.txt
compounds.txt:
	curl -s https://tokipona.org/compounds.txt > compounds.txt
nimi.json: o_ante_e_lipu_txt.py nimi_pu.txt nimi_pi_pu_ala.txt nimi_ku.txt
	python ./o_ante_e_lipu_txt.py | jq > nimi.json
nimi_lili.json: o_ante_e_lipu_txt.py nimi_pu.txt nimi_pi_pu_ala.txt nimi_ku.txt
	python ./o_ante_e_lipu_txt.py --maxsize=4 --minscore=40 | jq > nimi_lili.json

clean:
	rm -f nimi_pu.txt nimi_pi_pu_ala.txt compounds.txt nimi.json nimi_lili.json
