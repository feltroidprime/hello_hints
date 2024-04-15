// Retrieve a felt252 from a 4-element array of u64s
// No check is made the on the 4th element to ensure the value fits in Fp. 
fn parse_felt252(data: @Array<u64>) -> felt252 {
    assert!(data.len() == 4, "Invalid data length");
    let b0: felt252 = (*data.at(0)).into();
    let b1: felt252 = (*data.at(1)).into();
    let b2: felt252 = (*data.at(2)).into();
    let b3: felt252 = (*data.at(3)).into();
    let res: felt252 = b0
        + b1 * 18446744073709551616 // 2**64
        + b2 * 340282366920938463463374607431768211456 // 2**128
        + b3 * 6277101735386680763835789423207666416102355444464034512896; // 2**192
    return res;
}

