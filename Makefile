.PHONY: clean
clean:
	rm *.logs
	rm docs/*.logs
.PHONY: docs
docs:
	sphinx-apidoc -F -o docs assertionhelper
	cd docs && make clean && make html
