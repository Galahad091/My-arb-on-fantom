address = 0x7fa56BC2C9d69644ba31292a11dC174Bf6c1fdd7
//SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.4;
import "@openzeppelin/contracts/access/Ownable.sol";
// import "hardhat/console.sol";
interface IERC20 {
    // function totalSupply() external view returns (uint supply);
    function balanceOf(address _owner) external view returns (uint balance);
    function transfer(address _to, uint _value) external returns (bool success);
    function transferFrom(address _from, address _to, uint _value) external returns (bool success);
    function approve(address _spender, uint _value) external returns (bool success);
    // function allowance(address _owner, address _spender) external view returns (uint remaining);
    function decimals() external view returns(uint digits);
    event Approval(address indexed _owner, address indexed _spender, uint _value);
}

interface IUniswapV2Router {
  // function getAmountsOut(uint256 amountIn, address[] memory path) external view returns (uint256[] memory amounts);
  function swapExactTokensForTokens(uint256 amountIn, uint256 amountOutMin, address[] calldata path, address to, uint256 deadline) external returns (uint256[] memory amounts);
}

// interface IUniswapV2Pair {
//   function token0() external view returns (address);
//   function token1() external view returns (address);
//   function swap(uint256 amount0Out,  uint256 amount1Out, address to, bytes calldata data) external;
// }

contract PrintMoney is Ownable {

  //   function getAmountOutMin(address router, address _tokenIn, address _tokenOut, uint256 _amount) public view returns (uint256) {
    //  address[] memory path;
    //  path = new address[](2);
    //  path[0] = _tokenIn;
    //  path[1] = _tokenOut;
    //  uint256[] memory amountOutMins = IUniswapV2Router(router).getAmountsOut(_amount, path);
    //  return amountOutMins[path.length -1];
    // }
  
  //   function singleswap(address _router, address _tokenIn, address _tokenOut, uint256 _amount) private {
    //  IERC20(_tokenIn).approve(_router, _amount);
    //  address[] memory path;
    //  path = new address[](2);
    //  path[0] = _tokenIn;
    //  path[1] = _tokenOut;
    //  uint deadline = block.timestamp + 300;
    //  IUniswapV2Router(_router).swapExactTokensForTokens(_amount, 1, path, address(this), deadline);
    // }

    function unsafe_inc(uint x) private pure returns (uint) {
        unchecked { return x + 1;}
    }
    function multiswap(address[] memory router, address[][] calldata path, uint256 amountIn) onlyOwner external {
        // uint amountIn = optimalAmount;
        uint deadline = block.timestamp + 300;
        address basetoken = 0x5C7F8A570d578ED84E63fdFA7b1eE72dEae1AE23;
        uint startBalance = IERC20(basetoken).balanceOf(address(this));

        for(uint i=0; i < router.length; i = unsafe_inc(i)){
            if (i != 0){
            amountIn = IERC20(path[i][0]).balanceOf(address(this));
            }
            IERC20(path[i][0]).approve(router[i], amountIn); 
            IUniswapV2Router(router[i]).swapExactTokensForTokens(amountIn, 1, path[i], address(this), deadline);
            }   
                     
        uint endBalance = IERC20(basetoken).balanceOf(address(this));
        require(endBalance > startBalance, "Reverted, No Profit");
        }

    function withdraw(address tokenAddress) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        token.transfer(msg.sender, token.balanceOf(address(this)));
    }
    function getBalance (address _tokenContractAddress) external view  returns (uint256) {
        uint balance = IERC20(_tokenContractAddress).balanceOf(address(this));
        return balance;
    }
  // receive() payable external {}
    
    }

/////////////////////////////////////////////////////////////

address = 0x117a5d8C63B96d2912854c31CA12Fc1a9061d0C7

//SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.4;
import "@openzeppelin/contracts/access/Ownable.sol";
// import "hardhat/console.sol";
interface IERC20 {
    // function totalSupply() external view returns (uint supply);
    function balanceOf(address _owner) external view returns (uint balance);
    function transfer(address _to, uint _value) external returns (bool success);
    function transferFrom(address _from, address _to, uint _value) external returns (bool success);
    function approve(address _spender, uint _value) external returns (bool success);
    // function allowance(address _owner, address _spender) external view returns (uint remaining);
    function decimals() external view returns(uint digits);
    event Approval(address indexed _owner, address indexed _spender, uint _value);
}

interface IUniswapV2Router {
  function getAmountsOut(uint256 amountIn, address[] memory path) external view returns (uint256[] memory amounts);
  function swapExactTokensForTokens(uint256 amountIn, uint256 amountOutMin, address[] calldata path, address to, uint256 deadline) external returns (uint256[] memory amounts);
}

// interface IUniswapV2Pair {
//   function token0() external view returns (address);
//   function token1() external view returns (address);
//   function swap(uint256 amount0Out,  uint256 amount1Out, address to, bytes calldata data) external;
// }

contract PrintMoney is Ownable {

      function multiswap_Vm(address[] memory router, address[][] memory path, uint256[] memory amountIn) onlyOwner external {
        uint deadline = block.timestamp + 300;
        // uint256 [] memory amountOutMinlast;
        for(uint i=0; i < router.length; i = unsafe_inc(i)){
            
            IERC20(path[i][0]).approve(router[i], type(uint).max); 
            IUniswapV2Router(router[i]).swapExactTokensForTokens(amountIn[i], amountIn[i+1], path[i], address(this), deadline);
            }   
        // amountOutMinlast = IUniswapV2Router(router[router.length -1]).getAmountsOut(amountIn[amountIn.length-2], path[path.length -1]);       
        // require(amountOutMinlast[amountOutMinlast.length -1] > amountIn[0], "No Profit");
        }
      function unsafe_inc(uint x) private pure returns (uint) {
        unchecked { return x + 1;}
    }

      function withdraw(address tokenAddress) external onlyOwner {
      IERC20 token = IERC20(tokenAddress);
      token.transfer(msg.sender, token.balanceOf(address(this)));
      }
      function getBalance(address _tokenContractAddress) external view  returns (uint256) {
      uint balance = IERC20(_tokenContractAddress).balanceOf(address(this));
      return balance;
    }
     
    }


///////////////////////////////////////////////

0xa40247665AC78a64de399b5E2eCd9CD3284866b6

//SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.4;
import "@openzeppelin/contracts/access/Ownable.sol";
// import "hardhat/console.sol";
interface IERC20 {
    // function totalSupply() external view returns (uint supply);
    function balanceOf(address _owner) external view returns (uint balance);
    function transfer(address _to, uint _value) external returns (bool success);
    function transferFrom(address _from, address _to, uint _value) external returns (bool success);
    function approve(address _spender, uint _value) external returns (bool success);
    // function allowance(address _owner, address _spender) external view returns (uint remaining);
    function decimals() external view returns(uint digits);
    event Approval(address indexed _owner, address indexed _spender, uint _value);
}

interface IUniswapV2Router {
  function getAmountsOut(uint256 amountIn, address[] memory path) external view returns (uint256[] memory amounts);
//   function swapExactTokensForTokens(uint256 amountIn, uint256 amountOutMin, address[] calldata path, address to, uint256 deadline) external returns (uint256[] memory amounts);
}
interface IUniswapV2Pair {
  function token0() external view returns (address);
  function token1() external view returns (address);
  function swap(uint256 amount0Out,  uint256 amount1Out, address to, bytes calldata data) external;
}

contract Arbitrage1 is Ownable{

      function multiswap_Vm(address[] memory pairs, uint[] memory amount0Out, uint[] memory amount1Out, uint amountIn) onlyOwner external {
        // uint deadline = block.timestamp + 300;
        address basetoken = 0x5C7F8A570d578ED84E63fdFA7b1eE72dEae1AE23;
        address _to;
        IERC20(basetoken).transfer(pairs[0], amountIn);

        for(uint i=0; i < pairs.length; i = unsafe_inc(i)){  
          _to = i < (pairs.length -1) ? pairs[i+1] : address(this);         
            // if (i == pairs.length - 1){
            //     _to = address(this);
            // }
            // _to = pairs[i+1];
            IUniswapV2Pair(pairs[i]).swap(amount0Out[i], amount1Out[i], _to, new bytes(0));
            }   
        }
      function singleswap (address pair, uint amount0Out, uint amount1Out, uint amountIn) onlyOwner external {
        address basetoken = 0x5C7F8A570d578ED84E63fdFA7b1eE72dEae1AE23;
        IERC20(basetoken).transfer(pair, amountIn);
        IUniswapV2Pair(pair).swap(amount0Out, amount1Out, address(this), new bytes(0));

      }

      function unsafe_inc(uint x) private pure returns (uint) {
        unchecked { return x + 1;}
    }

      function withdraw(address tokenAddress) external onlyOwner {
      IERC20 token = IERC20(tokenAddress);
      token.transfer(msg.sender, token.balanceOf(address(this)));
      }
      function getBalance(address _tokenContractAddress) external view  returns (uint256) {
      uint balance = IERC20(_tokenContractAddress).balanceOf(address(this));
      return balance;
    }
     


}