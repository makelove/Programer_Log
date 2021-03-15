// https://blog.csdn.net/singleyellow/article/details/83714790
// 不是go语言
#include <stdio.h>
#include <Windows.h>

int main()
{
	// 壁纸格式给jpg也行，不像有些地方说的非要是bmp
	DWORD l_dwReturn=SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0,
	"C:\\Users\\work\\Downloads\\wp1.jpg" ,
	SPIF_UPDATEINIFILE);
	DWORD l_dwError=GetLastError();
	return 0;
}
