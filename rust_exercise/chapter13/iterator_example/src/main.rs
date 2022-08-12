fn main() {
    println!("Hello, world!");
    let v1 = vec![1, 2, 3];

    // iterators are lazy and do nothing unless consumed
    let mut v1_iter = v1.iter().map(|x| x+1);
    println!("{:?}", v1_iter);
    v1_iter.next();
    for item in v1_iter {
        println!("{}", item);
    }

    //
    let v1: Vec<i32> = vec![1, 2, 3];
    let v2: Vec<_> = v1.iter().map(|x| x + 1).collect();
    assert_eq!(v2, vec![2, 3, 4]);
}
