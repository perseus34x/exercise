address 0x16 {
module Structs {
    use Std::Debug::print;
    struct Foo has copy, drop { x: u64, y: bool }
    struct Bar has copy, drop { foo: Foo }
    struct Baz {}

    public fun read_write_fileds () {
        let foo = Foo { x: 3, y: true };
        let bar = Bar { foo: copy foo };
        let x: u64 = foo.x;
        let y: bool = foo.y;
        let foo2: Foo = bar.foo;
        print(&x);
        print(&y);
        print(&foo2);
    }
}
}