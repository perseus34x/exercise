pub fn primitive() {

    // varible can be type annotated.
    let logical: bool = true;
    let a_float: f64 = 1.0;

    println!("logical:{}", logical);
    println!("a_float:{}", a_float);


    // mutalbe varible
    let mut infered_type =12;
    println!("infered_type={}", infered_type);
    infered_type = 3456;
    println!("infered_type={}", infered_type);

    //shadowing
    let infered_type =true;
    println!("infered_type={}", infered_type);
    {
        let infered_type = false;
        println!("infered_type={}", infered_type);
        let infered_type = "abc";
        println!("infered_type={}", infered_type);
    }
    println!("infered_type={}", infered_type);

}
