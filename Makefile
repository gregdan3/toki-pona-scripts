init: nimi_pu.txt nimi_pi_pu_ala.txt
process: nimi.json

nimi_pu.txt:
	curl -s https://tokipona.org/nimi_pu.txt > nimi_pu.txt
nimi_pi_pu_ala.txt:
	curl -s https://tokipona.org/nimi_pi_pu_ala.txt > nimi_pi_pu_ala.txt
nimi.json: nasin_li_nimi.py nimi_pu.txt nimi_pi_pu_ala.txt
	python ./nasin_li_nimi.py | jq > nimi.json

clean:
	rm nimi_pu.txt nimi_pi_pu_ala.txt nimi.json
