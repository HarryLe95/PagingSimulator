.PHONY: clean

lru:
	@echo "Testing trace1-4frames-lru"
	@python memsim.py data/trace1 4 lru quiet > data/trace1_out
	@diff -bt data/trace1_out data/trace1-4frames-lru
	@echo "Testing trace1-8frames-lru"
	@python memsim.py data/trace1 8 lru quiet > data/trace1_out
	@diff -bt data/trace1_out data/trace1-8frames-lru
	@echo "Testing trace2-6frames-lru"
	@python memsim.py data/trace2 6 lru quiet > data/trace2_out
	@diff -bt data/trace2_out data/trace2-6frames-lru.ans
	@echo "Testing trace3-4frames-lru"
	@python memsim.py data/trace3 4 lru quiet > data/trace3_out
	@diff -bt data/trace3_out data/trace3-4frames-lru

clock:
	@echo "Testing trace 1 4 frames clock"
	@python memsim.py data/trace1 4 clock quiet > data/trace1_out
	@diff -bt data/trace1_out data/trace1-4frames-clock
	@echo "Testing trace 2 6 frames clock"
	@python memsim.py data/trace2 6 clock quiet > data/trace2_out
	@diff -bt data/trace2_out data/trace2-6frames-clock
	@echo "Testing trace 3 4 frames clock"
	@python memsim.py data/trace3 4 clock quiet > data/trace3_out
	@diff -bt data/trace3_out data/trace3-4frames-clock

clean:
	rm -rf data/trace*_out
	clear

# Test target that accepts a variable
.PHONY: pytest
pytest:
ifeq ($(filter pytest,$(MAKECMDGOALS)),pytest)
	$(eval file := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS)))
	$(if $(file),$(eval file := tests/test_$(file)),$(eval file := tests))
	@poetry run pytest $(file)
else
	@poetry run pytest
endif

tests: pytest lru clock