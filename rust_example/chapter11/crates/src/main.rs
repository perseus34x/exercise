fn main() {
    my::public_function();

    // Error! `private_function` is private
    //rary::private_function();
    my::indirect_access();
}
