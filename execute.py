from execute_1 import execute_1

filelist = ["(感覚の)表象の外在主義理論.md", "2.19 思考の様態について.md", "2.32 真である観念と偽である観念.md", "2.7 感覚と反省の双方からの単純観念.md", "4.1 知識一般について.md", "4.5 真理一般について.md", "4.7 公理.md", "4.8 くだらない命題について.md", "4.9 われわれがもつ現実存在の知識について.md", "CwS.md", "E1.4.20.md", "E2.1.19.md", "E2.1.4.md", "E2.10.2.md", "E2.19.1.md", "E2.19.3.md", "E2.32.15.md", "E2.32.19.md", "E2.32.2.md", "E2.32.3.md", "E2.33.19.md", "E2.7.7.md", "E2.9.4.md", "E4.1.4.md", "E4.1.5.md", "E4.17.8.md", "E4.2.1.md", "E4.2.14.md", "E4.21.4.md", "E4.5.2.md", "E4.7.4.md", "E4.8.2.md", "E4.8.3.md", "E4.9.3.md", "LoLordoの感覚、反省、意識の関係.md", "Mattern 1978.md", "Newman 2004.md", "Newman 2007.md", "Owen 1999.md", "Rickless 2008.md", "WS2016.md", "Weinberg 2016.md", "Will.md", "Wolterstorff 1996.md", "attention.md", "cleardistinct.md", "secret reference.md", "take notice of --example.md", "take notice.md", "trifling proposition.md", "冨田 1991.md", "命題.md", "快苦.md", "構成.md", "比較.md", "決意.md", "注目.md", "知識.md", "示唆.md", "肯定.md", "表象.md", "記号.md", "一目で.md", "対応説.md", "自己現前(WN96).md", "われあり.md", "意味表示.md", "構成要素.md", "知覚作用.md", "記憶の定義(2.10.2).md", "注目の定義(2.19.3).md", "秘密の関連(2.32.2).md", "知識の定義(4.1.2).md", "真理の定義(4.5.2).md", "くだらない.md", "一緒に置き.md", "同一性命題.md", "命題の定義.md", "最初の作用.md", "観念の知覚.md", "なんであるか.md", "付加的な知覚.md", "私の現実存在.md", "観念論的真理.md", "観念の一致の4カテゴリ(4.1.3).md", "意識は自己意識 i.e., 自分の思考が自分のものである経験.md", "くだらない命題.md", "個別事物の知識.md", "個別観念の知覚.md", "個別観念の知識.md", "現実存在の一致.md", "知覚の表象理論.md", "胎児も知覚する.md", "複合的心的状態.md", "逆転スペクトル.md", "最初の観念の定義(1.1.8).md", "全観念に伴う観念.md", "共存としての一致.md", "観念を同時に持つ.md", "関係としての一致.md", "「知性の探求は有用(1.1.1)」.md", "記述的で平明な方法(1.1.2).md", "ロック的コギト議論(4.9.3).md", "同一性としての一致.md", "観念の知識のパズル.md", "「心は意志と知性の2つの機能(能力)からなる(2.21.5)」.md", "最初の反省の特徴づけ(2.1.4).md", "観念のもう一つの源泉(2.1.4).md", "真理の語の通常の意味(2.32.3).md", "「知識は命題に存する(2.33.19)」.md", "子供の思考経験の記述.md", "観念の知覚の構成要素3つ.md", "空腹と空腹を感じること(2.1.19).md", "「知識は二観念間にのみ(NL,RS)」.md", "意識は全知覚の構成要素(WS16).md", "個別観念の同一性の知識.md", "形而上学的意味での真理.md", "意識は知覚作用の要素説.md", "観念知覚の一人称的特徴.md", "観念知覚は命題的である.md", "『知性論』の書かれた動機(1.1.2).md", "「注目は思考する心の状態(2.19.3)」.md", "真理の語の形而上学的意味(2.32.2).md", "「知性の作用はすべて知覚(2.6.2)」.md", "「知識は観念の一致の知覚(4.1.2)」.md", "「観念はすべて個別の実在(4.17.8)」.md", "感覚的知識の確実性の論証(4.2.14).md", "「記号を結合分離すること(4.5.2)」.md", "「同一性命題はくだらない(4.8.3)」.md", "表象理論の内容理論的解釈(Forrai05).md", "個別観念の現実存在の知識.md", "個別観念の知識を得る命題.md", "「観念は事物の現前する記号(4.21.4)」.md", "スティリングフリート宛書簡.md", "「すべての知覚は観念を含む」.md", "個別観念のなんであるかの知識.md", "注目・意識・記憶・人格同一性.md", "観念、語以外の記号もありえる.md", "観念は心のアクチュアルな知覚.md", "観念知覚の本来的で顕わな特徴.md", "記憶の特徴からの生得観念論批判(1.4.20).md", "「意識せずに幸不幸はありえない(2.1.11)」.md", "「主に観念と語が記号に使われる(2.32.19)」.md", "「注目は知覚作用とのかかわり方(WS16)」.md", "「観念概念の混合はロックの熟考(Yol.84)」.md", "「同一性と共存の一致の仕方は特異(4.1.7)」.md", "「すべての知覚は自己意識を含む」.md", "「個別観念を知ることは注目を要する(WS16)」.md", "「観念は知覚・思考・知性の直接的対象(2.8.8)」.md", "「観念の同一性の知識は心の最初の作用(4.1.4)」.md", "個別観念の知覚は複合的心的状態である(WS16).md", "「反省の観念の産出には注目を要する」.md", "「感覚の観念の産出には注目を要する」.md", "「注目とは観念が気づかれ記憶されること(2.19.1)」.md", "「逆転スペクトルは単純観念を偽にしない(2.32.15)」.md", "「命題は記号の結合分離で真理を作るもの(4.5.2)」.md", "最初に観念を持つ瞬間は、最初の感覚の時.md", "「観念の存在論的ステータスは問題ではない(W9.220)」.md", "意識は人間の心を過ぎゆくものの知覚である.md", "「現実存在と一性の観念は全観念で示唆される(2.7.7)」.md", "「直観的知識は心が視点を向けることを要する(4.2.1)」.md", "「ひとが知るまたは信念するものはすべて命題(CwS)」.md", "「自分が考えることを自分自身に意識している(E2.1.1)」.md", "「同一性は観念の気づきにとって基礎的である(OD99)」.md", "「既知の意識がない思い出しはもはや新しい観念(1.4.20)」.md", "「二観念間の関係の知覚なしに肯定的観念はない(4.1.5)」.md", "「全心的作用について、自分の存在を自己意識する(4.9.3)」.md", "「思い出しとは既知の意識をともなって知覚すること(1.4.20)」.md", "観念の同一性の知識を得る命題は、分析命題ではない(WS16).md", "「感覚の観念をもつときその外的原因を考えている」.md", "「観念の比較＝区別＝一致の知覚＝命題形成＝真理認識(OD99)」.md", "「観念の知覚の外部にその真理を保証するものはない」.md", "「意識が思考に伴い、自己を作り、他者との区別をつくる(2.27.9)」.md", "「観念の同一性を一目で、知覚と区別の力で直観的に知る(4.1.4)」.md", "「観念の実際の入り口の意識により別種の観念は区別可能(4.2.14)」.md", "「観念を区別することと直観知することを同じと見ている(WS16)」.md", "「この観念は私がそれを知覚しているとおりに存在する」.md", "「観念をそれ自体で知ることは心の最初の作用であり基礎的(4.7.4)」.md", "「直観的知識は観念が同時に持たれるだけで一目で知覚される(4.2.1)」.md", "「全知覚作用毎に、私の現実存在が意識され直観的に知られる(4.9.3)」.md", "「単純観念の実在性は実在物の構成と観念との定常的対応に存する(2.30.2)」.md", "「この観念は私の心内に知覚されるとおりのものとして現実存在する(SW16)」.md", "「特定の現実存在を知ることは、特定の観念を知ることと同じである(WS16)」.md", "「観念の一致は命題項間の一致と命題と現実存在の一致を混同している(MR78)」.md", "「個別観念を知るとき、いつ知性内にあるか・観念のなんであるかも知る(4.7.4)」.md", "「心にもつと意識するもの、それが知性に備え付けられる仕方を探求する」(1.1.3).md", "「直観的知識を得るためには、一致の要素を心に同時に持つことだけでよい(WS16)」.md", "「感覚から実際に来ている観念と記憶から復活している観念との違いは明らか(4.2.14)」.md", "「個別観念の形而上学的意味での真理の知識は個別観念の知覚の結果物である(WS16)」.md", "形而上学的真理を表現する命題が「この観念は私がそれを知覚しているように、ある」(WS16).md", "全観念の知覚の構成要素は、知覚される観念、現実存在の観念、それを知覚する意識の3つ(WS16).md", "「逆転スペクトルしていても観念が外的原因と規則的対応していればコミュニケーション可能(2.32.15)」.md", "「個別観念の知覚のさい、知覚される観念、現実存在の観念、意識が一目で心内に同時に得られる(WS16)」.md"]

for filename in filelist:
    execute_1(filename)