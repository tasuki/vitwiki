publish:
	./build.sh
develop:
	(cd build && php -S localhost:8321) & fd --type f --exclude build | SUFFIX=".html" entr ./build.sh
clean:
	rm -rf build/*
