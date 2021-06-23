package go

import (
	"alpha.dagger.io/dagger"
	"alpha.dagger.io/go"
	"alpha.dagger.io/alpine"
	"alpha.dagger.io/dagger/op"
)

TestData: dagger.#Artifact @dagger(input)

TestGoBuild: {
	build: go.#Build & {
		source: TestData
		output: "/bin/testbin"
	}

	test: #up: [
		op.#Load & {from: alpine.#Image},
		op.#Exec & {
			args: [
				"sh",
				"-ec",
				"""
					test "$(/bin/testbin)" = "hello world"
					""",
			]
			mount: "/bin/testbin": {
				from: build
				path: "/bin/testbin"
			}
		},
	]
}
