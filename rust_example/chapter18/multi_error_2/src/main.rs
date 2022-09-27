use std::num::ParseIntError;

// Option 1
fn double_first(vec: Vec<&str>) -> Option<Result<i32, ParseIntError>> {
    vec.first().map(|first| {first.parse::<i32>().map(|n| 2*n)} )
}

// Option 2
fn double_first_2(vec: Vec<&str>) -> Result<Option<i32>, ParseIntError> {
    let opt = vec.first().map(|first| {first.parse::<i32>().map(|n| 2*n)} );
    opt.map_or(Ok(None), |r| r.map(Some))
}

fn main() {
    // Output ==>
    //
    // The first doubled is Some(Ok(84))
    // The first doubled is None
    // The first doubled is Some(Err(ParseIntError { kind: InvalidDigit }))
    let numbers = vec!["42", "93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];
    println!("The first doubled is {:?}", double_first(numbers));
    println!("The first doubled is {:?}", double_first(empty));
    println!("The first doubled is {:?}", double_first(strings));

    // Output ==>
    //
    // The first doubled is Ok(Some(84))
    // The first doubled is Ok(None)
    // The first doubled is Err(ParseIntError { kind: InvalidDigit })
    let numbers_2 = vec!["42", "93", "18"];
    let empty_2 = vec![];
    let strings_2 = vec!["tofu", "93", "18"];
    println!("The first doubled is {:?}", double_first_2(numbers_2));
    println!("The first doubled is {:?}", double_first_2(empty_2));
    println!("The first doubled is {:?}", double_first_2(strings_2));
}
