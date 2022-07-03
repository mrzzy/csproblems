CXX_FLAGS:=-Wall -std=c++17 -O2 -g


.PHONY: test clean fmt


test: check_permutations
	./check_permutations

check_permutations: main.cpp
	$(CXX) $(CXX_FLAGS) $< -o $@

fmt: main.cpp
	clang-format -i $<

clean:
	rm -f check_permutations
