// modules/hello_world.move

address 0x6 {
module Vecs {
    use Std::Debug::print;

    struct Coin has drop,copy {
        value: u64,
    }
    public fun mint(value: u64): Coin {
        Coin { value }
    }

    public fun dump_info() {
        print(&b"world");
    }
}
} 