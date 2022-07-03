#
# makefile for c++
#

CXX_SOURCES:=$(wildcard *.cpp)
TARGETS:=$(basename $(CXX_SOURCES))
CXX_FLAGS:=-Wall -std=c++17 -O2 -g

.PHONY: all run clean fmt

run: $(TARGETS)
	$(addprefix ./,$(TARGETS))

all: $(TARGETS)

%: %.cpp
	$(CXX) $(CXX_FLAGS) $< -o $@

fmt: $(wildcard *.cpp)
	clang-format -i $^

clean:
	rm -f $(TARGETS)
