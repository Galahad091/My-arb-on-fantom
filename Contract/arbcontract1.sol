// SPDX-License-Identifier: MIT
pragma solidity 0.8.10;
import {IERC20, SafeERC20} from "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract AdvancedMultiTrade is Ownable {  
    using SafeERC20 for IERC20;

    // function approveToken(address token, address router_addr) onlyOwner external {
    //     IERC20 erc20 = IERC20(token);
    //     erc20.approve(router_addr, type(uint256).max); // usdt six decimal would fail!
    // }
    

    function swap(address[] memory tos, bytes[] memory data, address[] memory _tokenInaddr, uint256 inputamount) external payable {
      require(tos.length > 0 && tos.length == data.length, "Invalid input");
      require(tos.length > 0 && tos.length == _tokenInaddr.length, "Invalid input");
      for(uint256 i; i < tos.length; i++) {
        IERC20(_tokenInaddr[i]).approve(tos[i], type(uint256).max);
        (bool success,bytes memory returndata) = tos[i].call{value: inputamount, gas: gasleft()}(data[i]);
        require(success, string(returndata));
    }
  }

    receive() payable external {}

    function getSelector(string calldata _func) external pure returns (bytes4) {
    return bytes4(keccak256(bytes(_func)));

    }   
    function withdrawasset(address tokenAdress) external onlyOwner {
      IERC20 token = IERC20(tokenAdress);
      token.transfer(msg.sender, token.balanceOf(address(this)));

    }
}   
 