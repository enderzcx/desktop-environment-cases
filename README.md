# Desktop Environment Cases

收集真实桌面环境故障，把一次排障变成下一个产品可以复用的知识。

每个案例回答：出现什么症状、在哪些环境成立、有什么证据、怎样处理、如何确认恢复。案例适用于人和软件读取；收录不代表可以在用户机器上自动执行修复。

## 查找与复用

- [浏览案例](docs/INDEX.md)：已确认的问题与待复现的报告分开标明。
- [结构化索引](catalog.json)：按平台、类别、产品和关键词筛选，再读取对应的 `cases/*.json`。
- [行业参考](docs/REFERENCES.md)：兼容数据、环境采集和支持包的成熟方案。
- [历史补录范围](docs/HISTORY-IMPORT-2026-10-15.md)：本轮检查的来源、收录与合并方式、未计入项。
- [提交与审核](CONTRIBUTING.md)：从原始报告到有证据的案例。

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python tools/catalog.py search toSorted --confirmed
.venv/bin/python tools/catalog.py search 安装 --platform windows
```

Windows 激活虚拟环境后，用 `python` 执行相同命令；解释器位于 `.venv\Scripts\python.exe`。

## 记录约定

`cases/*.json` 是唯一编辑来源。`catalog.json`、`docs/INDEX.md`、`docs/cases/*.md` 由工具生成，CI 检查它们与源记录一致。结构见 [JSON Schema](schema/case.schema.json)。

| 状态 | 含义 |
| --- | --- |
| `reported` | 已有报告；根因尚未独立确认，可以检索，不能据此认定根因或自动修复 |
| `confirmed` | 至少有复现或代码分析证据确认根因；修复、发布、客户验收仍分别看证据 |
| `superseded` | 结论已被新证据或新案例取代，保留历史与替代说明 |

覆盖方向：运行时、安装与更新、存储权限与锁、GPU、媒体编解码、网络与 TLS、系统安全限制。只录有来源的案例；研究候选留在行业参考或 Issue 中。

接入产品时，先匹配环境和症状，再检查证据及适用限制。案例里的命令是供审核的说明，不是远程执行接口。未知版本和未检查状态必须保留为未知。

系统未记录时使用 `platforms: ["unknown"]`，不能猜填或混入已知系统。平台列表描述适用/涉及系统，不代表每个系统已经实机验收；请同时读环境和证据范围。类别描述问题所在层次，待定位报告的类别不表示已证明其环境根因。

## 本地检查

```sh
.venv/bin/python tools/catalog.py build
.venv/bin/python tools/catalog.py check
.venv/bin/python -m unittest discover -s tests -v
node --test reproducers/ENV-0001.test.mjs
```

最后一条在隔离 JavaScript 上下文模拟缺失 API，不启动应用、不读写用户数据，也不能代替真实 WebView2 验证。

## 数据与使用范围

仓库公开收集桌面环境故障，贡献提交按 [CONTRIBUTING](CONTRIBUTING.md) 审核。当前未授予公开再分发许可，第三方资料只保留必要事实摘要和来源链接。不要提交原始客户诊断包、聊天截图、姓名、账号、机器路径、请求正文、凭据或原始媒体。许可另行决定。
