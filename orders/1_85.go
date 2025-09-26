package main

import (
	"fmt"
	"log"

	"github.com/xuri/excelize/v2"
)

func main() {
	// Excel 文件路径
	filePath := `C:\ACT\公用核心\1.85_已经识别SKU品类.xlsx`
	sheetName := "整理当天全部订单"

	// 打开 Excel 文件
	f, err := excelize.OpenFile(filePath)
	if err != nil {
		log.Fatalf("打开文件失败: %v", err)
	}

	// 获取所有行
	rows, err := f.GetRows(sheetName)
	if err != nil {
		log.Fatalf("获取工作表行失败: %v", err)
	}

	// 找到 A-K 全空列的下一列
	targetCol := 11                 // 默认 L 列（0-based索引）
	for col := 0; col < 11; col++ { // A=0, K=10
		empty := true
		for _, row := range rows {
			if col < len(row) && row[col] != "" {
				empty = false
				break
			}
		}
		if empty {
			targetCol = col + 1 // 下一列
			break
		}
	}

	// 找该列第一个空行
	targetRow := 1 // Excel 行号从1开始
	found := false
	for r, row := range rows {
		if targetCol >= len(row) || row[targetCol] == "" {
			targetRow = r + 1 // 行号
			found = true
			break
		}
	}
	if !found {
		// 如果整列都不为空，下一行就是空行
		targetRow = len(rows) + 1
	}

	// 转换列索引到 Excel 字母列
	colLetter, err := excelize.ColumnNumberToName(targetCol + 1)
	if err != nil {
		log.Fatalf("转换列号失败: %v", err)
	}

	// 输出结果
	fmt.Printf("目标单元格: %s%d\n", colLetter, targetRow)
}
