script {
    use Std::Signer;
    fun sign(s: signer) {
        assert!(Signer::address_of(&s) == @0x42, 0);
    }
}