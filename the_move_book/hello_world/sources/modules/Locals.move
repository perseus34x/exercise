address 0x10 {
module Locals {

    use Std::Vector;
    struct S { f: u64, g: u64 }

    fun annotated() {
        let _u: u8 = 0;
        let _b: vector<u8> = b"hello";
        let _a: address = @0x0;
        let (_x, _y): (&u64, &mut u64) = (&0, &mut 1);
        let S { f: _f1, g: _f2 }: S = S { f: 0, g: 1 };

        let _v2: vector<u64> = Vector::empty(); // no error
    }
}
}