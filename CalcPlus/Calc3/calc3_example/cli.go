package main

import (
	"calcPlus/interpreter"
	"fmt"
	"os"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Fprintf(os.Stderr, "Usage: %s <calc3-file>\n", os.Args[0])
		os.Exit(1)
	}

	codeFile := os.Args[1]
	code, err := os.ReadFile(codeFile)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Failed to read file %s: %v\n", codeFile, err)
		os.Exit(1)
	}

	interpreter.RunCalc3Interpreter(string(code), os.Stdin, os.Stdout)
}
