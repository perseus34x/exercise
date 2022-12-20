address 0x11 {
module Equality {
    struct S has copy, drop { f: u64, s: vector<u8> }

    struct Coin has store { value: u64 }
    fun invalid(c1: Coin, c2: Coin): (Coin, Coin) {
        let are_equal = (&c1 == &c2);
        if(are_equal) (c1, c2) else (c2, c1) 
         // ERROR!
         //      ^^    ^^ These resources would be destroyed!
    }

    fun always_true(): bool {
        let s = S { f: 0, s: b"" };
        // parens are not needed but added for clarity in this example
        (copy s) == s
    }

    fun always_false(): bool {
        let s = S { f: 0, s: b"" };
        // parens are not needed but added for clarity in this example
        (copy s) != s
    }
}
}